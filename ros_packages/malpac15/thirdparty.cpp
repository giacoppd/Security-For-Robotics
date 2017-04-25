//General includes:
#include <iostream>
#include <stdio.h>
#include <string>

//Network related includes:
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>

//Target host details:
//need to figure out port.
#define PORT 1234
#define HOST "localhost"

using namespace std;


//Function prototypes:
string MessageFormat(int, char**);
void MessageSend(string);
string LittleEndian(string);

int main(int argc, char *argv[])
{
    //Big glob that comprises the mesasge. caller id? Message header? Field formatting? 
    string message = "message_definition=string data\n\ncallerid=/rostopic_4767_1316912741557latching=1md5sum=992ce8a1687cec8c8bd883ec73ca41d1topic=/chattertype=std_msgs/Stringhello";

    //Send the message out: 
    MessageSend(message);

    return 0;
}
//stolen from stack overflow, will need
void MessageSend(string message)
{
    int sd, ret;
    struct sockaddr_in server;
    struct in_addr ipv4addr;
    struct hostent *hp;

    sd = socket(AF_INET,SOCK_STREAM,0);
    server.sin_family = AF_INET;

    inet_pton(AF_INET, HOST, &ipv4addr);
    hp = gethostbyaddr(&ipv4addr, sizeof ipv4addr, AF_INET);
    //hp = gethostbyname(HOST);

    bcopy(hp->h_addr, &(server.sin_addr.s_addr), hp->h_length);
    server.sin_port = htons(PORT);

    connect(sd, (const sockaddr *)&server, sizeof(server));
    send(sd, (char *)message.c_str(), strlen((char *)message.c_str()), 0);
}
//stolen from stackoverflow, might not even need
string LittleEndian(string num)
{
    int number = Convert.ToInt32(num, 16);
    byte[] bytes = BitConverter.GetBytes(number);
    string retval = "";
    foreach (byte b in bytes)
        retval += b.ToString("X2");
    return retval;
}


