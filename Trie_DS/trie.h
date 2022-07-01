//
// Created by george on 24/06/2022.
//
#include <iostream>
#include "string.h"
#include "stdbool.h"
#include "unistd.h"
#include <string.h>
#include <time.h>
#include <list>
#include "stdlib.h"
#include "stdbool.h"
using namespace std;
#include <iostream>
#include <vector>
#include "math.h"
#include <memory>
using namespace std;
#define ALPHABET_SIZE 26


#ifndef UNTITLED36_TRIE_H
#define UNTITLED36_TRIE_H

class Trie_Node{
public:
    char c;
    bool isWord;
    int Total_words = 0;
    shared_ptr<Trie_Node> children[ALPHABET_SIZE];
    bool arr[ALPHABET_SIZE];//for DFS transversal
    Trie_Node(char c)
    {
        this->c = c;
        for (int i = 0; i < ALPHABET_SIZE; i++) {
            children[i] = shared_ptr<Trie_Node>();
            arr[i] = false;
        }
        isWord = false;
    }
};


class Trie {
public:
    // Storing root of the Trie
    shared_ptr<Trie_Node> root;

    Trie() {
        root = shared_ptr<Trie_Node>(new Trie_Node('/0'));
    }
    void Insert(string& trieString, shared_ptr<Trie_Node> root);
    void print_all_words_main(shared_ptr<Trie_Node> root);
    void print_all_words_aux(shared_ptr<Trie_Node> root);
    bool search_tool_main(shared_ptr<Trie_Node> root, string find);
    bool search_tool_aux(shared_ptr<Trie_Node> root, string find, int index);

    //Set array to zeros.
    void reset(shared_ptr<Trie_Node> root)
    {
        for(int i=0; i<=ALPHABET_SIZE; i++)
            root->arr[i] = 0;
    }


};

#endif //UNTITLED36_TRIE_H
