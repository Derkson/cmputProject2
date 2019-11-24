
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <cstring>

using namespace std;


int main ()
{
  string str;
  getline(cin,str);
  if(0 != str.compare("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")){
    cout << "You lose\n";
    return 1;
  }
  getline(cin,str);
  if(0 != str.compare("<emails type=\"array\">")){
    cout << "You lose to the second one\n";
    return 1;
  }

  //Here we've stripped the first two lines and now each line in the for loop will be an email line
  getline(cin,str);

  //Open the files
  ofstream datesfile;
  datesfile.open("dates.txt",fstream::app);
  ofstream emailsfile;
  emailsfile.open("emails.txt",fstream::app);
  ofstream recsfile;
  recsfile.open("recs.txt",fstream::app);
  ofstream termsfile;
  termsfile.open("terms.txt",fstream::app);

  //Set up set of valid chars for term comparison
  set<char> valid;
  char const * validList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_";
  valid.insert(validList, validList + strlen(validList));

  while (0 != str.compare("</emails>")) {
    //get the row
    int rowStart = str.find("<row>",6) + 5;
    int rowEnd = str.find("</row>",rowStart);
    int rowLen = rowEnd - rowStart;
    char row[rowLen + 1];
    row[rowLen] = '\0';
    str.copy(row, rowLen, rowStart);

    //Get the date
    int dateStart = str.find("<date>",rowEnd + 5) + 6;
    int dateEnd = str.find("</date>",dateStart);
    int dateLen = dateEnd - dateStart;
    char date[dateLen + 1];
    date[dateLen] = '\0';
    str.copy(date, dateLen, dateStart);

    //Get the from
    int fromStart = str.find("<from>",dateEnd + 6) + 6;
    int fromEnd = str.find("</from>",fromStart);
    int fromLen = fromEnd - fromStart;
    char from[fromLen + 1];
    from[fromLen] = '\0';
    str.copy(from, fromLen, fromStart);

    //Get the to
    int toStart = str.find("<to>",fromEnd + 6) + 4;
    int toEnd = str.find("</to>",toStart);
    int toLen = toEnd - toStart;
    char to[toLen + 1];
    to[toLen] = '\0';
    str.copy(to, toLen, toStart);

    //Get the subj
    int subStart = str.find("<subj>",toEnd + 4) + 6;
    int subEnd = str.find("</subj>",subStart);
    int subLen = subEnd - subStart;
    char sub[subLen + 1];
    sub[subLen] = '\0';
    str.copy(sub, subLen, subStart);

    //Get the cc
    int ccStart = str.find("<cc>",subEnd + 6) + 4;
    int ccEnd = str.find("</cc>",ccStart);
    int ccLen = ccEnd - ccStart;
    char cc[ccLen + 1];
    cc[ccLen] = '\0';
    str.copy(cc, ccLen, ccStart);

    //Get the bcc
    int bccStart = str.find("<bcc>",ccEnd + 4) + 5;
    int bccEnd = str.find("</bcc>",bccStart);
    int bccLen = bccEnd - bccStart;
    char bcc[bccLen + 1];
    bcc[bccLen] = '\0';
    str.copy(bcc, bccLen, bccStart);

    //Get the body!!
    int bodyStart = str.find("<body>",bccEnd + 5) + 6;
    int bodyEnd = str.find("</body>",bodyStart);
    int bodyLen = bodyEnd - bodyStart;
    char body[bodyLen + 1];
    body[bodyLen] = '\0';
    str.copy(body, bodyLen, bodyStart);


    //Print the str to rec
    recsfile << row << ":" << str << '\n';

    //Print to date
    datesfile << date << ":" << row << '\n';

    //Print to terms
    //sub
    if (subLen != 0) {
      string tempsub = "";
      bool ignore = false; //A boolean for if we're in an ignored term
      for (int i = 0; i < subLen; i++) {
        if ('&' == sub[i]) {
          ignore = true;
          if (tempsub.length() > 2) {
            termsfile << "s-" << tempsub << ":" << row << "\n";
          }
          tempsub = "";
        }
        else if (ignore == false) {
          if (valid.count(sub[i]) == 1) {
            tempsub.push_back(tolower(sub[i]));
          }
          else {
            if (tempsub.length() > 2) {
              termsfile << "s-" << tempsub << ":" << row << "\n";
            }
            ignore = false;
            tempsub = "";
          }
        }
        else if (';' == sub[i]) {
          ignore = false;
        }
      }
      if (tempsub.length() > 2) {
        termsfile << "s-" << tempsub << ":" << row << "\n";
      }
    }

    //body
    if (bodyLen != 0) {
      string tempbody = "";
      bool ignore = 0; //A boolean for if we're in an ignored term
      for (int i = 0; i < bodyLen; i++) {
        if ('&' == body[i]) {
          ignore = true;
          if (tempbody.length() > 2) {
            termsfile << "b-" << tempbody << ":" << row << "\n";
          }
          tempbody = "";
        }
        else if (ignore == false) {
          if (valid.count(body[i]) == 1) {
            tempbody.push_back(tolower(body[i]));
          }
          else {
            if (tempbody.length() > 2) {
              termsfile << "b-" << tempbody << ":" << row << "\n";
            }
            ignore = false;
            tempbody = "";
          }
        }
        else if (';' == body[i]) {
          ignore = false;
        }
      }
      if (tempbody.length() > 2) {
        termsfile << "b-" << tempbody << ":" << row << "\n";
      }
    }


    //Print to emails
    //from
    emailsfile << "from-" << from << ':' << row << '\n';

    //to
    if (toLen != 0) {
      string tempto = "";
      for (int i = 0; i < toLen; i++) {
        if (',' == to[i]) {
          emailsfile << "to-" << tempto << ":" << row << "\n";
          tempto = "";
        }
        else{
          tempto.push_back(tolower(to[i]));
        }
      }
      emailsfile << "to-" << tempto << ":" << row << "\n";
    }

    //cc
    if (ccLen != 0) {
      string tempcc = "";
      for (int i = 0; i < ccLen; i++) {
        if (',' == cc[i]) {
          emailsfile << "cc-" << tempcc << ":" << row << "\n";
          tempcc = "";
        }
        else{
          tempcc.push_back(tolower(cc[i]));
        }
      }
      emailsfile << "cc-" << tempcc << ":" << row << "\n";
    }

    //bcc
    if (bccLen != 0) {
      string tempbcc = "";
      for (int i = 0; i < bccLen; i++) {
        if (',' == bcc[i]) {
          emailsfile << "bcc-" << tempbcc << ":" << row << "\n";
          tempbcc = "";
        }
        else{
          tempbcc.push_back(tolower(bcc[i]));
        }
      }
      emailsfile << "bcc-" << tempbcc << ":" << row << "\n";
    }


    //Get the next email line
    getline(cin,str);
  }
  //Close the files
  datesfile.close();
  emailsfile.close();
  recsfile.close();
  termsfile.close();

  cout << "End\n";
  return 0;
}
