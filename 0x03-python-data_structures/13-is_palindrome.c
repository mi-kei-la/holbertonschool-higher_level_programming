#include "lists.h"

/**
* is_palindrome - check if single linked list is palindrome
*
* @head: pointer to start of list
* Return: 1 if not palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	int i, x = 1, y = 0, *array;
	listint_t *tmp = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	array = malloc(sizeof(int));
	while (tmp)
	{
		array = realloc(array, sizeof(int) * x);
		array[y] = tmp->n;
		x++;
		y++;
		tmp = tmp->next;
	}

	y = y - 1;
	for (i = 0; i <= y; i++, y--)
	{
		if (array[i] != array[y])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
