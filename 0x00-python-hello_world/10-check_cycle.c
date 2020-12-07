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
	listint_t *fast_and_furious = list;

	if (list == NULL)
		return (0);

	while (fast_and_furious->next->next != NULL)
	{
		if (list->next == fast_and_furious->next->next)
			return (1);
		list = list->next;
		fast_and_furious = fast_and_furious->next->next;
	}
	return (0);
}

