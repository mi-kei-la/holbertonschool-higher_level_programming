#include "lists.h"

/**
* is_palindrome - check if single linked list is palindrome
*
* @head: pointer to start of list
* Return: 1 if palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	int i, x = 0, y = 0, count;

	count = _count(*head);
	count = count - 1;
	
	for (i = 0; i < count; i++)
	{
		x = indexer(*head, i);
		y = indexer(*head, (count - i));
		if (x != y)
			return (0);
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

/**
 * indexer - return data of node at index
 * 
 * @head: pointer to start of list
 * @index: node to retrieve
 * 
 * Return: data
 */

int indexer(listint_t *head, int index)
{
	int x, ret = 0;

	for (x = 0; x < index && head != NULL; x++)
		head = head->next;
	ret = head->n;
	return (ret);
}
