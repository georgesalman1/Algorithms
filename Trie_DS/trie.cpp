// Created by george on 25/06/2022.
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
#include "trie.h"
int counter = 0;
bool flag  = false;

int i2c(char c)
{
    return static_cast<int>(c - 'a');
}

void Trie::Insert(string& trieString, shared_ptr<Trie_Node> root)
{
    shared_ptr<Trie_Node> current = root;
    for (int i = 0; i < trieString.size(); i++)
    {
        // If word after some prefix is not
        // present then creates new node
        if (current->children[i2c(trieString[i])] == shared_ptr<Trie_Node>(nullptr))
        {
            current->children[i2c(trieString[i])] = shared_ptr<Trie_Node>(new Trie_Node(trieString[i]));
        }
        current = (current->children[i2c(trieString[i])]);
    }
    current->isWord = true;
    root->Total_words+=1;

}

void Trie::print_all_words_main(shared_ptr<Trie_Node> root) {
    cout<<"Words in trie:"<<endl;
    shared_ptr<Trie_Node> current = root;
    vector<shared_ptr<Trie_Node>> transversal;
        for (int i = 0; i < ALPHABET_SIZE; i++) {
            if (current->children[(i)] != shared_ptr<Trie_Node>(nullptr)) {
                current->arr[i] = true;
                print_all_words_aux(current->children[i]);
            }
        }
    reset(root);
    counter = 0;
}


void Trie::print_all_words_aux(shared_ptr<Trie_Node> root)
{

    for(int i = 0; i < ALPHABET_SIZE; i++) {
        if (root->children[(i)] != shared_ptr<Trie_Node>(nullptr) && root->arr[i] == false) {
            if (flag == false) {
                cout << counter << ". ";
                flag = true;
            }
            cout << root->c;
            root->arr[i] = true;
            if (root->children[i]->isWord == true) {
                cout << root->children[i]->c;
                cout << "\n";
                counter = counter + 1;
                flag = false;
                //a word generated;
            }

            print_all_words_aux(root->children[i]);
        }
        if(i==ALPHABET_SIZE-1)
            reset(root);
    }
}

bool Trie::search_tool_main(shared_ptr<Trie_Node> root, string find){
    shared_ptr<Trie_Node> current = root;

    for (int i = 0; i < find.size(); i++)
    {
        // If at any point in Trie Node for particular
        // character is not present means nullptr then
        // return false
        if (current->children[i2c(find[i])] == shared_ptr<Trie_Node>(nullptr))
            return false;
        current = current->children[i2c(find[i])];
    }

    // At the end of the word checking whether this
    // word is really present or not
    if (current->isWord == true)
        return true;

    return false;
}




