import data

# Write your functions for each part in the space below.

# Part 1
import data
# Part 1: create_rectangle
def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle:
    """
    Determine the top-left and bottom-right points from any two points and return a Rectangle object.
    Input: Two points (point1, point2) of type Point.
    Output: A Rectangle with the top-left and bottom-right corners determined.
    """
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)
    bottom_right_x = max(point1.x, point2.x)
    bottom_right_y = min(point1.y, point2.y)

    top_left = data.Point(top_left_x, top_left_y)
    bottom_right = data.Point(bottom_right_x, bottom_right_y)
    return data.Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(duration1: data.Duration, duration2: data.Duration) -> bool:
    """
    Compares two durations to determine if the first is shorter than the second.
    Input: Two durations (duration1, duration2) of type Duration.
    Output: True if duration1 is shorter than duration2, False otherwise.
    """
    total_seconds_1 = duration1.minutes * 60 + duration1.seconds
    total_seconds_2 = duration2.minutes * 60 + duration2.seconds
    return total_seconds_1 < total_seconds_2

# Part 3
def songs_shorter_than(songs: list[data.Song], max_duration: data.Duration) -> list[data.Song]:
    """
    Filters a list of songs to return those with a duration less than the specified max duration.
    Input: A list of songs and a maximum duration (type Duration).
    Output: List of songs shorter than max_duration.
    """
    return [song for song in songs if shorter_duration_than(song.duration, max_duration)]

# Part 4
def running_time(songs: list[data.Song], playlist_indices: list[int]) -> data.Duration:
    """
    Calculates the total running time of the specified songs in a playlist.
    Input: A list of songs and a list of indices indicating the playlist.
    Output: A Duration object representing the total running time.
    """
    total_seconds = 0
    for index in playlist_indices:
        if 0 <= index < len(songs):  # Check if index is within range
            song = songs[index]
            total_seconds += song.duration.minutes * 60 + song.duration.seconds

    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return data.Duration(minutes, seconds)

# Part 5
def add_song(songs: list[data.Song], artist: str, title: str, duration: data.Duration) -> None:
    """
    Adds a new song to the list of songs.
    Input: List of songs, artist name (string), title (string), and duration (type Duration).
    Output: None. The song is added to the list.
    """
    new_song = data.Song(artist, title, duration)
    songs.append(new_song)


# Part 6
# Part 6: remove_song
def remove_song(songs: list[data.Song], artist: str, title: str) -> bool:
    """
    Removes a song by artist and title from the list if it exists.
    Input: List of songs, artist name (string), title (string).
    Output: True if the song was found and removed, False otherwise.
    """
    for i, song in enumerate(songs):
        if song.artist == artist and song.title == title:
            songs.pop(i)
            return True
    return False

