#include "lists.h"

/**
  * check_cycle - check if there is a loop in a linked list
  *
  * @list: pointer to head
  *
  * Return: 1 if loop, 0 if no loop
  */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *furious = list;

	if (list != NULL)
	{
/*		while (fast->next != NULL && furious->next != NULL) */
		while (1)
		{
			fast = fast->next;
			furious = furious->next;
			if (furious->next == NULL)
				break;
			furious = furious->next;
			if (furious == fast)
				return (1);
		}
	}
	return (0);
}

