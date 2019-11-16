
#include <iostream>
#include <fstream>
#include <string>

//using namespace std;

//Copied
#include <vector>
#include <string>
#include <cstring>
using namespace std;

/**
 * @brief Tokenize a string
 *
 * @param str - The string to tokenize
 * @param delim - The string containing delimiter character(s)
 * @return std::vector<std::string> - The list of tokenized strings. Can be empty
 */
std::vector<std::string> tokenize(const std::string &str, const char *delim) {
  char* cstr = new char[str.size() + 1];
  std::strcpy(cstr, str.c_str());

  char* tokenized_string = strtok(cstr, delim);

  std::vector<std::string> tokens;
  while (tokenized_string != NULL)
  {
    tokens.push_back(std::string(tokenized_string));
    tokenized_string = strtok(NULL, delim);
  }
  delete[] cstr;

  return tokens;
}
//Copied
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

  ofstream file;
  while (0 != str.compare("</emails>")) {
    //Initialize the variables
    int rowStart = str.find("<row>",6) + 5;
    int rowEnd = str.find("</row>",rowStart);
    int rowLen = rowEnd - rowStart;
    char row[rowLen + 1];
    row[rowLen] = '\0';
    str.copy(row, rowLen, rowStart);

    //Get the date Alex, GET THE DATE!!
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
    file.open("recs.txt",fstream::app);
    file << row << ":" << str << '\n';
    file.close();

    //Print to date
    file.open("dates.txt",fstream::app);
    file << date << ":" << row << '\n';
    file.close();

    //Print to terms
    file.open("terms.txt",fstream::app);
    std::vector<std::string> termsvector;
    std::string subterms(sub);
    termsvector = tokenize(subterms," ");
    file << "s-" << termsvector[0] << ":" << row << '\n';
    file.close();


    //Get the next email line
    getline(cin,str);
  }
  cout << "End\n";
  return 0;
}
