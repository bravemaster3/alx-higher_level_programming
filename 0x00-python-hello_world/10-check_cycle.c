#include "lists.h"
/**
 * check_cycle - checks for the presence of a cycle in the list
 * @list: pointer to the head of the list
 * Return: 0 if no cycle found, 1 if a cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return (0);
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
