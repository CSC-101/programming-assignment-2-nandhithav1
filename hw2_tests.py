import unittest
import data
import hw2


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        point1 = data.Point(2, 2)
        point2 = data.Point(10, 10)
        rectangle = hw2.create_rectangle(point1, point2)
        self.assertEqual(rectangle.top_left, data.Point(2, 10))
        self.assertEqual(rectangle.bottom_right, data.Point(10, 2))

    # Part 2
    def test_shorter_duration_than(self):
        duration1 = data.Duration(2, 30)
        duration2 = data.Duration(3, 15)
        self.assertTrue(hw2.shorter_duration_than(duration1, duration2))

        duration1 = data.Duration(3, 20)
        duration2 = data.Duration(3, 15)
        self.assertFalse(hw2.shorter_duration_than(duration1, duration2))

    # Part 3
    def test_songs_shorter_than(self):
        song1 = data.Song('Artist1', 'Title1', data.Duration(3, 20))
        song2 = data.Song('Artist2', 'Title2', data.Duration(4, 0))
        song3 = data.Song('Artist3', 'Title3', data.Duration(2, 45))
        songs = [song1, song2, song3]
        max_duration = data.Duration(3, 30)

        result = hw2.songs_shorter_than(songs, max_duration)
        self.assertEqual(result, [song1, song3])

    # Part 4
    def test_running_time(self):
        song1 = data.Song('Artist1', 'Title1', data.Duration(4, 30))
        song2 = data.Song('Artist2', 'Title2', data.Duration(3, 40))
        song3 = data.Song('Artist3', 'Title3', data.Duration(3, 29))
        songs = [song1, song2, song3]
        playlist_indices = [0, 2, 1, 2]

        total_duration = hw2.running_time(songs, playlist_indices)
        self.assertEqual(total_duration, data.Duration(15, 8))

    # Part 5
    def test_add_song(self):
        songs = [
            data.Song('Artist1', 'Title1', data.Duration(4, 30)),
            data.Song('Artist2', 'Title2', data.Duration(3, 40))
        ]
        hw2.add_song(songs, 'Artist3', 'Title3', data.Duration(2, 45))

        # Check that the song was added correctly
        self.assertEqual(len(songs), 3)
        self.assertEqual(songs[-1].artist, 'Artist3')
        self.assertEqual(songs[-1].title, 'Title3')
        self.assertEqual(songs[-1].duration, data.Duration(2, 45))

    # Part 6
    # Tests for remove_song
    def test_remove_song(self):
        songs = [
            data.Song('Artist1', 'Title1', data.Duration(4, 30)),
            data.Song('Artist2', 'Title2', data.Duration(3, 40)),
            data.Song('Artist3', 'Title3', data.Duration(2, 45))
        ]

        # Attempt to remove a song that exists
        removed = hw2.remove_song(songs, 'Artist2', 'Title2')
        self.assertTrue(removed)
        self.assertEqual(len(songs), 2)
        self.assertNotIn(data.Song('Artist2', 'Title2', data.Duration(3, 40)), songs)

        # Attempt to remove a song that does not exist
        removed = hw2.remove_song(songs, 'Artist4', 'Title4')
        self.assertFalse(removed)
        self.assertEqual(len(songs), 2)  # Length should remain the same


if __name__ == '__main__':
    unittest.main()
