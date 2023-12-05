#ifndef LIST_H
#define LIST_H

typedef struct listint_t
{
    int data;
    struct listint_t *next;
} listint_t;

listint_t *reverse_second_half(listint_t *head);
int is_palindrome(listint_t **head);
void push(listint_t **head, int data);
void print_list(listint_t *head);

#endif /* LIST_H */
