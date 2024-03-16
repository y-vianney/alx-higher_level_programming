#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: Head of the linked list
 * @number: The value of the node to add
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current = NULL;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	new_node->n = number;
	new_node->next = NULL;

	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
