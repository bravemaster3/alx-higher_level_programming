#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head
 * Return: 1 if a palindrome, 0 if not a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = list_len(head), i = 0, mid;
	listint_t *ptr, *ptr_r, *temp, *ctr, *ctr_cpy;

	if (len <= 1)
		return (1);

	if (len % 2 == 0)
		mid = len / 2 - 1;
	else
		mid = len / 2;

	ptr = *head;
	while (ptr != NULL)
	{
		if (i == mid)
		{
			ctr = ptr;
			ctr->next = NULL;
			ctr_cpy = ctr;
			temp = ptr->next;
		}
		if (i > mid)
		{
			ptr_r = temp;
			temp = 

			ptr->next = NULL;
			ptr = temp
		}
		i++;
		ptr = ptr->next;
	}

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
