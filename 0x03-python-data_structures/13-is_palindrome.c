#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head
 * Return: 1 if a palindrome, 0 if not a palindrome
 */
int is_palindrome(listint_t **head)
{
	int l = list_len(head), a[1501], i = 0, n1, n2;
	listint_t *ptr, *n;

	if (l <= 1)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		if (i < l / 2)
		{
			a[i] = ptr->n;
			i++;
		}
		if (i == l / 2)
			i--;
		else
		{
			i--;
			n1 = ptr->n;
			n = NULL;
			if (ptr->next != NULL)
			{
				n2 = ptr->next->n;
				n = ptr->next;
			}
			if ((l % 2 == 0 && a[i] != n1) || (n && l % 2 != 0 && a[i] != n2))
				return (0);
		}
		ptr = ptr->next;
	}
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
