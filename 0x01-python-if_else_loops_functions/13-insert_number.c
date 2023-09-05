#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in an ordered int list
 * @head: pointer to the pointer to head
 * @number: the number to be inserted
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	if (head == NULL)
		return (NULL);
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (current == NULL)
	{
		*head = new;
		return (*head);
	}
	while (current->next != NULL)
	{
		if (current->next->n < number)
			current = current->next;
		else
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
	}
	current->next = new;
	return (new);
}
