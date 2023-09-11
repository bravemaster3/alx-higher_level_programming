#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head
 * Return: 1 if a palindrome, 0 if not a palindrome
 */
int is_palindrome(listint_t **head)
{
	int l = list_len(head), *a, i = 0, j = l / 2, n1, n2;
	listint_t *ptr, *n;

	if (l <= 1)
		return (1);
	ptr = *head;
	a = malloc(sizeof(int) * l);
	if (a == NULL)
		return (-1);
	while (ptr != NULL)
	{
		if (i < l / 2)
			a[i] = ptr->n;
		i += 1;
		if (i > l / 2)
		{
			j -= 1;
			n1 = ptr->n;
			n = NULL;
			if (ptr->next != NULL)
			{
				n2 = ptr->next->n;
				n = ptr->next;
			}
			if ((l % 2 == 0 && a[j] != n1) || (n && l % 2 != 0 && a[j] != n2))
			{
				free(a);
				return (0);
			}
		}
		ptr = ptr->next;
	}
	free(a);
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
