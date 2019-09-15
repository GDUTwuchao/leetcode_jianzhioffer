/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        ListNode *p;
        ListNode *q;
        ListNode *r;
        p = pHead;
        q = NULL;
        while(p){
            r = p->next;
            p->next = q;
            q = p;
            p = r;
        }
        pHead = q;
        return pHead;
    }
};

