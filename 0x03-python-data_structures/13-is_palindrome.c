#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_second_half(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next_node;
    while (current != NULL)
    {
        next_node = current->next;
        current->next = prev;
        prev = current;
        current = next_node;
    }
    return prev;
}

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
    {
        return 1;
    }

    listint_t *slow = *head, *fast = *head, *prev_slow = *head;
    listint_t *second_half, *reversed_second_half;

    while (fast != NULL && fast->next != NULL)
    {
        prev_slow = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    second_half = slow;
    reversed_second_half = reverse_second_half(second_half);

    while (reversed_second_half != NULL)
    {
        if ((*head)->data != reversed_second_half->data)
        {
            return 0;
        }
        *head = (*head)->next;
        reversed_second_half = reversed_second_half->next;
    }

    reversed_second_half = reverse_second_half(second_half);
    prev_slow->next = reversed_second_half;

    return 1;
}

void push(listint_t **head, int data)
{
    listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}

void print_list(listint_t *head)
{
    while (head != NULL)
    {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}