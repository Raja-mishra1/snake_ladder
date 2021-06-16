class Snake:
    def add_snake(self,start,dest):
        """[Add snake to game]

        Args:
            start ([str]): [starting point of snake]
            dest ([str]): [ending point of snake]

        Raises:
            ValueError: [description]

        Returns:
            snakes [dict]: [dictionary of snake]
        """
        snakes = dict()
        if start>dest:
            snakes[start] = dest
        else:
            raise ValueError('Snake destination greater than start point')
        return snakes
    
    def __repr__(self):
        return self.snakes