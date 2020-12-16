#include "lists.h"
/**
 * is_palindrome - Check if linked list is palindrome or not
 * @head: head pointer
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = (*head);
	int array[2048];
	int y = 0, z;
	
	if (!head)
		return (1);
	while (tmp)
	{
		array[y] = tmp->n;
		y++;
		tmp = tmp->next;
	}
	y--;
	for (z = 0; z <= y; y--, z++)
	{
		if (array[z] != array[y])
			return (0);
	}
	return (1);
}
