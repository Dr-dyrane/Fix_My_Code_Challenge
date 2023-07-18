#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>
#include <string.h>

/**
 * struct dlistint_s - Doubly linked list node structure.
 * @n: Integer stored in the node.
 * @prev: Pointer to the previous element of the list.
 * @next: Pointer to the next element of the list.
 *
 * Description: Doubly linked list node structure.
 */
typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;

/* Function prototypes */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index);
size_t print_dlistint(const dlistint_t *h);
void free_dlistint(dlistint_t *head);
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n);

#endif /* LISTS_H */
