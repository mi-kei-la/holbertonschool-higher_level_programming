#include "lists.h"

/**
* is_palindrome - check if single linked list is palindrome
*
* @head: pointer to start of list
* Return: 1 if palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	int count = _count(*head), i, j, x;
	listint_t *tmp = *head, *last = NULL;

	count = count - 1;
	if (count % 2 == 0)
		x = count / 2;
	else
		x =(count + 1) / 2;
	
	for (i = 0; i < x; i++)
	{
		last = *head;
		for (j = 0; j < (count - i); j++)
			last = last->next;
		if (tmp->n != last->n)
			return (0);
		else
			tmp = tmp->next;
	}
	return (1);
}

/**
* _count - count nodes
*
* @head: pointer to head
* Return: number of nodes
*/

int _count(listint_t *head)
{
	int x = 0;

	while (head)
	{
		head = head->next;
		x++;
	}
	return (x);
}
