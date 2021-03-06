#include "lists.h"

/**
  * insert_node - insert node in an ordered list
  *
  * @head: start of list
  * @number: data
  *
  * Return: pointer to new node, NULL otherwise
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *dub = NULL;
	listint_t *new = malloc(sizeof(listint_t));

	if (head == NULL || new == NULL)
		return (NULL);

	if (tmp == NULL || number <= tmp->n)
	{
		*head = add_node(head, number);
		return (*head);
	}

	while (tmp != NULL)
	{
		dub = tmp;
		if (tmp->next == NULL)
		{
			new->n = number;
			new->next = NULL;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
		if (tmp->n >= number)
		{
			new->n = number;
			new->next = tmp;
			dub->next = new;
			return (new);
		}
		else
			dub = dub->next;
	}
	return (NULL);
}

/**
  * add_node - add node at start of list
  *
  * @head: head of list
  * @num: value of node
  *
  * Return: pointer to new node, NULL otherwise
  */

listint_t *add_node(listint_t **head, int num)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = num;
	new->next = *head;
	*head = new;

	return (new);
}
