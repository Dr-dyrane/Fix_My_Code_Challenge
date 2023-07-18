#include <stdlib.h>
#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes a node at a given index in a doubly linked list.
 * @head: Pointer to the head node of the list.
 * @index: Index of the node to be deleted.
 * Return: 1 if success, -1 if failure.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *temp, *current = *head;

    if (*head == NULL)
        return (-1);

    if (index == 0)
    {
        *head = current->next;
        if (current->next)
            current->next->prev = NULL;
        free(current);
        return (1);
    }

    while (index > 0 && current != NULL)
    {
        current = current->next;
        index--;
    }

    if (current == NULL)
        return (-1);

    temp = current->prev;
    temp->next = current->next;

    if (current->next != NULL)
        current->next->prev = temp;

    free(current);
    return (1);
}
