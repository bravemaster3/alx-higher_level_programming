#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head
 * Return: 1 if a palindrome, 0 if not a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = list_len(head), *rev_list, i = 0;
	listint_t *ptr;

	if (len <= 1)
		return (1);
	ptr = *head;
	rev_list = malloc(sizeof(int) * len);
	while (ptr != NULL)
	{
		rev_list[len - 1 - i] = ptr->n;
		i += 1;
		ptr = ptr->next;
	}
	ptr = *head;
	i = 0;
	while (ptr != NULL)
	{
		if (ptr->n != rev_list[i])
		{
			free(rev_list);
			return (0);
		}
		i += 1;
		ptr = ptr->next;
	}
	free(rev_list);
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
