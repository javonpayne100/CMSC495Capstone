import unittest
import numpy as np
import json
from TicTacToe import mark_cell, is_cell_empty, check_win, is_board_full, board
from Breakout import Block, Ball, Striker, collisionChecker, populateBlocks

class TestTicTacToe(unittest.TestCase):
    def test_mark_and_check_cell(self):
        board[:, :] = 0
        mark_cell(0, 0, 1)
        self.assertFalse(is_cell_empty(0, 0))

    def test_win_conditions(self):
        board[:, :] = 0
        board[0] = [1, 1, 1]  # Simulate a win on the first row
        self.assertTrue(check_win(1))

    def test_board_full(self):
        board[:, :] = 1  # Fill board
        self.assertTrue(is_board_full())


class TestTrivia(unittest.TestCase):
    def test_questions_json_structure(self):
        with open("Questions.json", "r") as file:
            data = json.load(file)

        self.assertIsInstance(data, dict)
        for category, questions in data.items():
            self.assertIsInstance(questions, list)
            for q in questions:
                self.assertIn("question", q)
                self.assertIn("answers", q)
                self.assertIn("correct", q)
                self.assertIsInstance(q["answers"], list)
                self.assertIsInstance(q["correct"], int)
                self.assertTrue(0 <= q["correct"] < len(q["answers"]))

    def test_trivia_answer_index(self):
        sample_question = {
            "question": "Sample?",
            "answers": ["A", "B", "C", "D"],
            "correct": 2
        }
        self.assertEqual(sample_question["answers"][sample_question["correct"]], "C")


class TestBreakout(unittest.TestCase):
    def test_block_health_reduction(self):
        block = Block(0, 0, 40, 20, (255, 0, 0))
        original_health = block.getHealth()
        block.hit()
        self.assertEqual(block.getHealth(), original_health - 100)

    def test_block_destruction(self):
        block = Block(0, 0, 40, 20, (0, 255, 0))
        while block.getHealth() > 0:
            block.hit()
        self.assertLessEqual(block.getHealth(), 0)

    def test_ball_reset(self):
        ball = Ball(200, 200, 5, 5, (255, 255, 255))
        ball.reset()
        self.assertEqual((ball.posx, ball.posy), (0, 450))
        self.assertEqual((ball.xFac, ball.yFac), (1, -1))

    def test_ball_bounce_off_wall(self):
        ball = Ball(0, 200, 5, 5, (255, 255, 255))
        ball.xFac = -1
        ball.update()
        self.assertEqual(ball.xFac, 1)

    def test_ball_hit_paddle(self):
        ball = Ball(100, 100, 5, 5, (255, 255, 255))
        ball.yFac = 1
        ball.hit()
        self.assertEqual(ball.yFac, -1)

    def test_striker_position_bounds(self):
        striker = Striker(0, 0, 100, 20, 10, (255, 255, 255))
        striker.posx = -50
        striker.posx = max(0, min(striker.posx, 750 - striker.width))
        self.assertGreaterEqual(striker.posx, 0)

        striker.posx = 1000
        striker.posx = max(0, min(striker.posx, 750 - striker.width))
        self.assertLessEqual(striker.posx, 750 - striker.width)

    def test_collision_detection(self):
        block = Block(100, 100, 40, 20, (0, 255, 0))
        ball = Ball(110, 110, 5, 5, (255, 255, 255))
        self.assertTrue(collisionChecker(block.getRect(), ball.getRect()))

    def test_populate_blocks(self):
        blocks = populateBlocks(40, 15, 10, 10)
        self.assertGreater(len(blocks), 0)
        for block in blocks:
            self.assertIsInstance(block, Block)


if __name__ == '__main__':
    unittest.main()
