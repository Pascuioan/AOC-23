#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <utility>

struct gear{
    int nums, x, y;
};

bool isSymbol(char x){
    if((x < 'a' || x > 'z') && (x < 'A' || x > 'Z') && x != '.'){
        if((x < '0') || (x > '9'))
            return true;
    }
    return false;
}

bool isDigit(char x){
    return x >= '0' && x <= '9';
}

int getNum(char * row, int & startIndex){
    int num = 0;
    while((row[startIndex] != '.') && !isSymbol(row[startIndex])){
        num = num * 10 + (row[startIndex] - '0');
        startIndex++;
    }
    return num;
}

void part1(){
    std::ifstream in("input.txt");
    std::string s;
    int sum = 0, startOfSequence;
    in>>s;
    int n = s.length();
    in.close();
    in.open("input.txt");

    char ** matrix = new char* [n + 2];
    for(int i = 0; i < n + 2; i++){
        matrix[i] = new char[n + 2];
        if(i == 0 || i == n + 1){
            for(int j = 0; j < n + 2; j++)
                matrix[i][j] = '.';    
        }else{
            for(int j = 1; j < n + 1; j++)
                in>>matrix[i][j];
            matrix[i][0] = '.';
            matrix[i][n + 1] = '.';
        }
    }

    for(int i = 0; i < n + 2; i++){
        startOfSequence = -1;
        for(int j = 0; j < n + 2; j++){
            if(isDigit(matrix[i][j])){
                if(startOfSequence == -1)
                    startOfSequence = j;
                if(isSymbol(matrix[i][j + 1]) || isSymbol(matrix[i][j - 1]) || isSymbol(matrix[i - 1][j]) ||isSymbol(matrix[i + 1][j]) || 
                   isSymbol(matrix[i + 1][j + 1]) || isSymbol(matrix[i + 1][j - 1]) || isSymbol(matrix[i - 1][j - 1]) ||isSymbol(matrix[i - 1][j + 1])){
                    j = startOfSequence;
                    sum += getNum(matrix[i], j);
                    startOfSequence = -1;
                   }
            }else{
                startOfSequence = -1;
            }
        } 
    }
    std::cout<<sum<<'\n';
}

void part2(){
    std::map<std::pair<int, int>, gear> gears;
    std::ifstream in("input.txt");
    std::string s;
    int sum = 0, startOfSequence;
    in>>s;
    int n = s.length();
    in.close();
    in.open("input.txt");

    char ** matrix = new char* [n + 2];
    for(int i = 0; i < n + 2; i++){
        matrix[i] = new char[n + 2];
        if(i == 0 || i == n + 1){
            for(int j = 0; j < n + 2; j++)
                matrix[i][j] = '.';    
        }else{
            for(int j = 1; j < n + 1; j++)
                in>>matrix[i][j];
            matrix[i][0] = '.';
            matrix[i][n + 1] = '.';
        }
    }

    for(int i = 0; i < n + 2; i++){
        startOfSequence = -1;
        for(int j = 0; j < n + 2; j++){
            if(isDigit(matrix[i][j])){
                if(startOfSequence == -1)
                    startOfSequence = j;
                for(int iOff = -1 ; iOff <= 1; iOff++){
                    for(int jOff = -1; jOff <= 1; jOff++){
                        if(iOff == 0 && jOff == 0)
                            continue;
                        if(matrix[i + iOff][j + jOff] == '*'){
                            auto g = gears.find(std::make_pair(i + iOff, j + jOff));
                            if(g != gears.end()){
                                g->second.nums++;
                                j = startOfSequence;
                                startOfSequence = -1;
                                g->second.y = getNum(matrix[i], j);
                                break;
                            }else{
                                gear g;
                                auto gIt = gears.insert(std::make_pair(std::make_pair(i + iOff, j + jOff), g));
                                gIt.first->second.nums = 1;
                                j = startOfSequence;
                                startOfSequence = -1;
                                gIt.first->second.x = getNum(matrix[i], j);
                                break;
                            }
                        }
                    }
                    if(startOfSequence == -1)
                        break;
                }
            }else{
                startOfSequence = -1;
            }
        }
    }
    for(auto gear : gears){
        if(gear.second.nums == 2)
            sum += gear.second.x * gear.second.y;
    }
    std::cout<<sum;
}

int main(){
    part2();
}