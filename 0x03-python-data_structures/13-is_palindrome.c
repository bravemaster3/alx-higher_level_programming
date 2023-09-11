#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head
 * Return: 1 if a palindrome, 0 if not a palindrome
 */
int is_palindrome(listint_t **head)
{
    int len = list_len(head), l = 3000, rev_list[l], i = l - 1;
    listint_t *ptr;

    if (len <= 1)
        return (1);
    ptr = *head;
    if (rev_list == NULL)
        return (-1);
    while (ptr != NULL)
    {
        rev_list[i] = ptr->n;
        i--;
        ptr = ptr->next;
    }
    ptr = *head;
    i++;
    while (ptr != NULL)
    {
        if (ptr->n != rev_list[i])
            return (0);
        i += 1;
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
