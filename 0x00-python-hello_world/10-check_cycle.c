#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: Linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *next_next;

	if (list == NULL)
		return (0);

	current = list;
	next_next = list->next;

	while (next_next && next_next->next)
	{
		if (current == next_next)
			return (1);

		current = current->next;
		next_next = next_next->next->next;
	}

	return (0);
}
