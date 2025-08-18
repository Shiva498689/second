#include <iostream>
#include <string>
using namespace std;

void encode()
{
    string s, str = "";
    int val;
    cout << "please input your message" << endl;
    cin >> s;
    cout << "please input your Key Number" << endl;
    cin >> val;

    int len = s.length();
    for (int i = 1; i <= len; i++)
    {
        char c = s[i - 1];
        if (int(c) >= 65 and (int)(c) <= 90)
        {
            int ascii = (int)(c);
            if (ascii + val <= 90)
            {
                str += char(ascii + val);
            }

            else
            {
                int n = -91 + (ascii + val) + 65;
                str += char(n);
            }
        }
        else if (char(c) >= 97 and char(c) <= 122)
        {
            int ascii = int(c);
            if (ascii + val <= 122)
            {
                str += char(ascii + val);
            }
            else
            {
                int n = ascii + val - 122 + 96;
                str += char(n);
            }
        }
        else
            str += c;
    }
    cout << "Your encoded Message is: " << str;
}
void decode()
{
    string s, str = "";
    int val;
    cout << "please input your message" << endl;
    cin >> s;
    cout << "please input your Key Number" << endl;
    cin >> val;

    int len = s.length();

    for (int i = 1; i <= len; i++)
    {
        char c = s[i - 1];
        if (int(c) >= 65 and (int)(c) <= 90)
        {
            int ascii = (int)(c);
            if (ascii - val >= 65)
            {
                str += char(ascii - val);
            }

            else
            {
                int n = 91 - (65 - (ascii - val));
                str += char(n);
            }
        }
        else if (char(c) >= 97 and char(c) <= 122)
        {
            int ascii = int(c);
            if (ascii - val >= 97)
            {
                str += char(ascii - val);
            }
            else
            {
                int n = (ascii - val) - 96 + 122;
                str += char(n);
            }
        }
        else
            str += c;
    }
    cout << "Your Decoded Message is: " << str;
}
int main()
{
    string inp;
    cout << "if you want to encode a message than enter \"encode\" " << endl;
    cout << "if you want to decode a message than enter \"decode\" " << endl;
    cin >> inp;
    if (inp == "decode")
        decode();
    if (inp == "encode")
        encode();
    return 0;
}