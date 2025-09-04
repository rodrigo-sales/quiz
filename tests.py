import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# Novo Teste 1
def test_create_question_with_custom_points_and_max_selections():
    question = Question(title='q1', points=100, max_selections=5)
    
    assert question.points == 100
    assert question.max_selections == 5
    assert question.title == 'q1'

# Novo Teste 2
def test_add_multiple_choices_with_sequential_ids():
    question = Question(title='q1')
    
    choice1 = question.add_choice('a')
    choice2 = question.add_choice('b')
    
    assert choice1.id == 1
    assert choice2.id == 2
    assert len(question.choices) == 2

# Novo Teste 3
def test_remove_all_choices_from_question():
    question = Question(title='Test Question')
    question.add_choice('a')
    question.add_choice('b')
    
    question.remove_all_choices()
    assert len(question.choices) == 0

# Novo Teste 4
def test_add_choice_with_empty_text_exception():
    question = Question(title='q1')
    
    with pytest.raises(Exception, match='Text cannot be empty'):
        question.add_choice('')

# Novo Teste 5
def test_add_choice_with_long_text_exception():
    question = Question(title='q1')
    long_text = 'a' * 101
    
    with pytest.raises(Exception, match='Text cannot be longer than 100 characters'):
        question.add_choice(long_text)

# Novo Teste 6
def test_remove_choice_with_valid_id():
    question = Question(title='q1')
    choice = question.add_choice('a')
    
    question.remove_choice_by_id(choice.id)
    assert len(question.choices) == 0

# Novo Teste 7
def test_remove_choice_with_invalid_id_exception():
    question = Question(title='q1')
    question.add_choice('a')
    
    with pytest.raises(Exception, match='Invalid choice id 9999'):
        question.remove_choice_by_id(9999)

# Novo Teste 8
def test_set_correct_choices_with_valid_ids():
    question = Question(title='q1')
    choice1 = question.add_choice('a')
    choice2 = question.add_choice('b')
    choice3 = question.add_choice('c')
    
    question.set_correct_choices([choice1.id, choice3.id])
    
    assert choice1.is_correct == True
    assert choice2.is_correct == False
    assert choice3.is_correct == True

# Novo Teste 9
def test_correct_selected_choices_with_single_correct_answer():
    question = Question(title='q1', max_selections=1)
    correct_choice = question.add_choice('a_correct', True)
    wrong_choice = question.add_choice('b_wrong', False)
    
    result = question.correct_selected_choices([correct_choice.id])
    
    assert result == [correct_choice.id]
    assert len(result) == 1

# Novo Teste 10
def test_correct_selected_choices_exceeds_max_selections_exception():
    question = Question(title='q1', max_selections=2)
    choice1 = question.add_choice('a')
    choice2 = question.add_choice('b')
    choice3 = question.add_choice('c')
    
    with pytest.raises(Exception, match='Cannot select more than 2 choices'):
        question.correct_selected_choices([choice1.id, choice2.id, choice3.id])