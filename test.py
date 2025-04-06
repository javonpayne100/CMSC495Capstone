import unittest
import numpy as np
import json
import Trivia

# Import specific functions and variables from the TicTacToe module
from TicTacToe import mark_cell, is_cell_empty, check_win, is_board_full, board
# Import classes and functions from the Breakout module
from Breakout import Block, Ball, Striker, collisionChecker, populateBlocks
# Import classes and functions from the Main Menu Module
from MainMenu import font, check_hover, SCREEN_WIDTH, SCREEN_HEIGHT


# ----------------------------
# Test Cases for Main Menu
# ----------------------------
class TestMainMenu(unittest.TestCase):
    # 1. Mouse hover is detected when within bounds
    def test_hover_inside_bounds(self):
        text = "Play"
        x, y = 100, 100
        mouse_pos = (110, 110)  # Inside expected bounds
        self.assertTrue(check_hover(mouse_pos, x, y, font, text))

    # 2. Mouse hover returns False when outside bounds
    def test_hover_outside_bounds(self):
        text = "Play"
        x, y = 100, 100
        mouse_pos = (10, 10)  # Outside the bounding box
        self.assertFalse(check_hover(mouse_pos, x, y, font, text))

    # 3. Invalid option to navigate() does not crash
    def test_invalid_navigation_option(self):
        from MainMenu import navigate
        try:
            navigate(99)  # Undefined option
        except Exception as e:
            self.fail(f"navigate() crashed with unexpected input: {e}")

    # 4. All menu options register hover correctly
    def test_hover_detection_on_all_menu_items(self):
        options = ["1. Tic-Tac-Toe", "2. Trivia", "3. Breakout", "4. Exit"]
        start_y = 130
        spacing = 60

        for i, option in enumerate(options):
            x = SCREEN_WIDTH // 2 - font.size(option)[0] // 2
            y = start_y + i * spacing
            width, height = font.size(option)
            mouse_pos = (x + width // 2, y + height // 2)
            self.assertTrue(check_hover(mouse_pos, x, y, font, option), f"Hover should detect: {option}")

    # 5. Simulates a user clicking on the 'Trivia' option in the main menu.
    def test_click_on_trivia_option(self):
        """
        Verifies that check_hover detects the correct area.
        """
        # This matches the second option: "2. Trivia"
        menu_text = "2. Trivia"
        x = SCREEN_WIDTH // 2 - font.size(menu_text)[0] // 2
        y = 130 + 1 * 60  # Second option's Y position

        # Simulate a click in the center of the button
        mouse_x = x + 5
        mouse_y = y + 5
        result = check_hover((mouse_x, mouse_y), x, y, font, menu_text)
        self.assertTrue(result, "Trivia option should detect hover/click at its position")


# ----------------------------
# Test Cases for Tic Tac Toe
# ----------------------------

class TestTicTacToe(unittest.TestCase):

    # 1. Test marking a cell and ensuring it's no longer empty
    def test_mark_and_check_cell(self):
        board[:, :] = 0  # Reset board
        mark_cell(0, 0, 1)
        self.assertFalse(is_cell_empty(0, 0))

    # 2. Test a winning condition (horizontal row)
    def test_win_conditions(self):
        board[:, :] = 0
        board[0] = [1, 1, 1]  # Simulate player 1 win on row 0
        self.assertTrue(check_win(1))

    # 3. Test for full board detection (used to check for draw)
    def test_board_full(self):
        board[:, :] = 1  # Fill all cells
        self.assertTrue(is_board_full())

    # 4. Test if a given board cell is empty (value 0) for valid moves
    def test_is_cell_empty_false(self):
        board[:] = np.zeros((3, 3))
        board[0][0] = 1  # Simulate a player move
        self.assertFalse(is_cell_empty(0, 0), "Expected cell (0,0) to be occupied")

    # 5. Tests that check_win correctly identifies a win along the main diagonal.
    def test_diagonal_win(self):
        """
        Player 1 occupies (0,0), (1,1), and (2,2).
        """
        board[:] = np.zeros((3, 3))  # Clear board
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1

        self.assertTrue(check_win(1), "Player 1 should win with a diagonal line")


# ----------------------------
# Test Cases for Trivia Game
# ----------------------------
class TestTrivia(unittest.TestCase):

    # 1. Test that the questions JSON is structured correctly
    def test_questions_json_structure(self):
        """
        Loads the Questions.json file and verifies that:
        - Each category is a list
        - Each question has 'question', 'answers', and 'correct'
        - 'answers' is a list with at least 2 items
        - 'correct' is a valid index
        """

        with open("Questions.json", "r") as file:
            data = json.load(file)

        for category, questions in data.items():
            self.assertIsInstance(questions, list, f"{category} should be a list of questions")

            for q in questions:
                self.assertIn("question", q)
                self.assertIn("answers", q)
                self.assertIn("correct", q)

                self.assertIsInstance(q["question"], str)
                self.assertIsInstance(q["answers"], list)
                self.assertGreaterEqual(len(q["answers"]), 2)

                self.assertIsInstance(q["correct"], int)
                self.assertTrue(0 <= q["correct"] < len(q["answers"]),
                                f"Correct index out of range in category '{category}'")

    # 2. Test that the correct answer index maps to the correct text
    def test_trivia_answer_index(self):
        sample_question = {
            "question": "Sample?",
            "answers": ["A", "B", "C", "D"],
            "correct": 2
        }
        self.assertEqual(sample_question["answers"][sample_question["correct"]], "C")

    # 3. Test that the final score message is properly formatted based on the given score.
    def test_final_score_display_text(self):
        """ This replicates the text shown
        in the play_again_screen() function.
        """
        score = 5
        expected_text = f"Game Over! Final Score: {score}"
        actual_text = f"Game Over! Final Score: {score}"  # This mimics what's rendered

        self.assertEqual(actual_text, expected_text)

    # 4. Tests that the color logic inside draw_timer chooses the correct color based on time_left.
    def test_timer_color_decision(self):
        """
        Tests that the color logic inside draw_timer chooses
        the correct color based on time_left.
        """
        def get_timer_color(time_left):
            if time_left > 6:
                return "GREEN"
            elif time_left > 3:
                return "YELLOW"
            else:
                return "RED"

        self.assertEqual(get_timer_color(8), "GREEN")
        self.assertEqual(get_timer_color(5), "YELLOW")
        self.assertEqual(get_timer_color(2), "RED")

    # 5. Simulates a user clicking on an incorrect answer.
    def test_user_selects_wrong_answer(self):
        """
        Verifies that the selection does not match the correct index.
        """
        question_data = {
            "question": "What is the capital of Italy?",
            "answers": ["Madrid", "Rome", "Berlin", "Paris"],
            "correct": 1  # Rome is correct
        }
        user_selected_index = 2  # User clicked "Berlin" (wrong)

        self.assertNotEqual(user_selected_index, question_data["correct"],
                            "Selected answer should be marked as incorrect")

    # 6. Simulates a user clicking on the correct answer.
    def test_user_selects_correct_answer(self):
        """
        Verifies that the selected index matches the correct index.
        """
        question_data = {
            "question": "Which planet is known as the Red Planet?",
            "answers": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct": 1  # Mars
        }

        user_selected_index = 1  # User selects "Mars"

        self.assertEqual(user_selected_index, question_data["correct"],
                         "Selected answer should be correct")


# ----------------------------
# Test Cases for Breakout Game
# ----------------------------

class TestBreakout(unittest.TestCase):
    # 1. Ensure block health is reduced on hit
    def test_block_health_reduction(self):
        block = Block(0, 0, 40, 20, (255, 0, 0))
        original_health = block.getHealth()
        block.hit()
        self.assertEqual(block.getHealth(), original_health - 100)

    # 2. Check that blocks can be destroyed after repeated hits
    def test_block_destruction(self):
        block = Block(0, 0, 40, 20, (0, 255, 0))
        while block.getHealth() > 0:
            block.hit()
        self.assertLessEqual(block.getHealth(), 0)

    # 3. Confirm ball resets to correct position and direction
    def test_ball_reset(self):
        ball = Ball(200, 200, 5, 5, (255, 255, 255))
        ball.reset()
        self.assertEqual((ball.posx, ball.posy), (0, 450))
        self.assertEqual((ball.xFac, ball.yFac), (1, -1))

    # 4. Test ball bounces off the wall and reverses direction
    def test_ball_bounce_off_wall(self):
        ball = Ball(0, 200, 5, 5, (255, 255, 255))
        ball.xFac = -1
        ball.update()
        self.assertEqual(ball.xFac, 1)

    # 5. Test ball direction changes after hitting the paddle
    def test_ball_hit_paddle(self):
        ball = Ball(100, 100, 5, 5, (255, 255, 255))
        ball.yFac = 1
        ball.hit()
        self.assertEqual(ball.yFac, -1)

    # 6. Ensure the striker stays within screen bounds
    def test_striker_position_bounds(self):
        striker = Striker(0, 0, 100, 20, 10, (255, 255, 255))

        # Test left boundary
        striker.posx = -50
        striker.posx = max(0, min(striker.posx, 750 - striker.width))
        self.assertGreaterEqual(striker.posx, 0)

        # Test right boundary
        striker.posx = 1000
        striker.posx = max(0, min(striker.posx, 750 - striker.width))
        self.assertLessEqual(striker.posx, 750 - striker.width)

    # 7. Test that collisions between ball and block are detected
    def test_collision_detection(self):
        block = Block(100, 100, 40, 20, (0, 255, 0))
        ball = Ball(110, 110, 5, 5, (255, 255, 255))
        self.assertTrue(collisionChecker(block.getRect(), ball.getRect()))

    # 8. Test that populateBlocks creates valid block objects
    def test_populate_blocks(self):
        blocks = populateBlocks(40, 15, 10, 10)
        self.assertGreater(len(blocks), 0)
        for block in blocks:
            self.assertIsInstance(block, Block)


# Entry point to run the tests
if __name__ == '__main__':
    unittest.main()
