#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head
 * Return: 1 if a palindrome, 0 if not a palindrome
 */
int is_palindrome(listint_t **head)
{
	int l = list_len(head), i = 0, j, n1, n2;
	listint_t *ptr, *n, *cpy2 = NULL, **cpy = &cpy2;

	if (l <= 1)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		if (i < l / 2)
			cpy2 = add_nodeint(cpy, ptr->n);
		i += 1;
		if (i > l / 2)
		{
			j = cpy2->n;
			n1 = ptr->n;
			n = NULL;
			if (ptr->next != NULL)
			{
				n2 = ptr->next->n;
				n = ptr->next;
			}
			if ((l % 2 == 0 && j != n1) || (n && l % 2 != 0 && j != n2))
			{
				free_listint(cpy2);
				return (0);
			}
			if (cpy2->next)
				cpy2 = cpy2->next;
		}
		ptr = ptr->next;
	}
	free_listint(cpy2);
	return (1);
}

/**
 * list_len - checks the length of a linked list
 * @head: the double pointer to the head
 * Return: the number of nodes in the linked list
 */
int list_len(listint_t **head)
{
	int len = 0;
	listint_t *ptr;

	if (head == NULL)
		return (len);
	ptr = *head;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		len += 1;
	}
	return (len);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}
