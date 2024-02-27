#include <iostream>
#include <fstream>
#include <cstring>

int ctoi(char c){
    switch (c)
    {
    case '0':
        return 0;
    case '1':
        return 1;
    case '2':
        return 2;
    case '3':
        return 3;
    case '4':
        return 4;
    case '5':
        return 5;
    case '6':
        return 6;
    case '7':
        return 7;
    case '8':
        return 8;
    case '9':
        return 9;
    default:
        return -1;
    }
}

int wtoi(char * w){
    if(!strcmp(w, "one"))
        return 1;
    if(!strcmp(w, "two"))
        return 2;
    if(!strcmp(w, "three"))
        return 3;
    if(!strcmp(w, "four"))
        return 4;
    if(!strcmp(w, "five"))
        return 5;
    if(!strcmp(w, "six"))
        return 6;
    if(!strcmp(w, "seven"))
        return 7;
    if(!strcmp(w, "eight"))
        return 8;
    if(!strcmp(w, "nine"))
        return 9;
    return -1;
}

void part1(std::istream & in){
    int sum = 0, index, last, digit, first;
    char line[256];

    while(in>>line){
        index = 0;
        while(line[index]){
            if((digit = ctoi(line[index])) != -1){
                first = digit;
                break;
            }
            index++;
        }
        while(line[index]){
            if((digit = ctoi(line[index])) != -1)
                last = digit;
            index++;
        }
        sum += first * 10 + last;
    }
    std::cout<<sum;
}

void part2(std::istream & in){
    int sum = 0;
    short first, last;
    char line[256], digits[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'},
         words[9][6] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"},
         *firstDigit, *lastDigit, *pointer;

    while(in>>line){
        lastDigit = 0;
        firstDigit = (char *)0xffffffff;
        for(auto ch : digits){
            pointer = strchr(line, ch);

            if(!pointer)
                continue;

            //first occurance
            if(pointer < firstDigit){//if it appears earlier than any other
                firstDigit = pointer;
                first = ctoi(ch);
            }

            //last occurance
            while(strchr(pointer + 1, ch) != NULL)
                pointer = strchr(pointer + 1, ch);
            
            if(pointer > lastDigit){//if it appears later than any other
                lastDigit = pointer;
                last = ctoi(ch);
            }
            
        }

        for(auto word : words){
            pointer = strstr(line, word);

            if(!pointer)
                continue;

            if(pointer < firstDigit){
                firstDigit = pointer;
                first = wtoi(word);
            }

            while(strstr(pointer + 1, word) != NULL)
                pointer = strstr(pointer + 1, word);
            
            if(pointer > lastDigit){//if it appears later than any other
                lastDigit = pointer;
                last = wtoi(word);
            }

        }

        sum += first * 10 + last;
    }

    std::cout<<sum;
}

int main(){
    std::ifstream in("input.txt");
    part2(in);
}