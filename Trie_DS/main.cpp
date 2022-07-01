#include <iostream>
#include <iostream>
#include "string.h"
#include "stdbool.h"
#include "unistd.h"
#include <string.h>
#include <time.h>
#include <list>
#include "stdlib.h"
#include "stdbool.h"
#include "string.h"
using namespace std;
#include <iostream>
#include <vector>
#include "trie.h"
#include "math.h"
int main() {
    Trie* node = new Trie();
    string geo = "happy";
    string geo1 = "hasppy";
    string geo2 = "george";
    string geo3 = "sososoososo";
    string geo4 = "basma";
    string geo5 = "zzzs";
    string geo6 = "zzzsdfssscs";

    //Small test
    node->Insert(geo, node->root);
    node->Insert(geo1, node->root);
    node->Insert(geo2, node->root);
    node->Insert(geo3, node->root);
    node->Insert(geo4, node->root);
    node->Insert(geo5, node->root);



    //small test of the interface
    cout<<"\n";
    node->print_all_words_main(node->root);
    cout<<node->search_tool_main(node->root, geo4)<<endl;
    node->Insert(geo6, node->root);


    node->print_all_words_main(node->root);


}
