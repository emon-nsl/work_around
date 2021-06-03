#include <stdio.h>
// struct node
// {
//   int roll;
// 	node *next;
// };
// node *root=NULL;

struct node
{
	int roll;
	node *next, *prev;
};
node *root, *tail;
// this append takes constant time to append new node
void append(int roll)
{
	if(root==NULL) //If the list is empty
	{
		root=new node();
		root->roll=roll;
		root->next=NULL;
		tail=root;
	}
	else
	{
		node *newnode=new node();
		newnode->roll=roll;
		newnode->next=NULL;
		tail->next=newnode; //add the new node after tail node
		tail=tail->next; //move tail pointer forward
	}
}


void print()
{
		node *current_node=root;
		while(current_node!=NULL) //loop until you reach null
		{
			printf("%d\n",current_node->roll);
			current_node=current_node->next;
		}
}

void delete_node(int roll)
{
	node *current_node=root;
	node *previous_node=NULL;
	while(current_node->roll!=roll) //Searching node 
	{
		previous_node=current_node; //Save the previous node
		current_node=current_node->next;
	}
	if(current_node==root) //Delete root
	{
		node *temp=root; //save root in temporary variable
		root=root->next; //move root forward
		delete(temp); //free memory
	}
	else //delete non-root node
	{
		previous_node->next=current_node->next; //previous node points the current node's next node 
		delete(current_node); //free current node
	}
	
}

int main(){

	append(1);
	append(2);
	append(6);
	print();
// 	printf("hi there\n");
	delete_node(1);
	print();
    return 0;
}
