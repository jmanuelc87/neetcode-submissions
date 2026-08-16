/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node * cur = head;
        unordered_map<Node *, Node *> oldToCopy;
        oldToCopy[NULL] = NULL;

        while (cur != nullptr)
        {
            oldToCopy[cur] = new Node(cur->val);
            cur = cur->next;
        }

        cur = head;

        while (cur != nullptr)
        {
            Node * copy = oldToCopy[cur];
            copy->next = oldToCopy[cur->next];
            copy->random = oldToCopy[cur->random];
            cur = cur->next;
        }

        return oldToCopy[head];
    }
};
