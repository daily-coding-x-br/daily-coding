class Node:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

        self.locked = False
        self.num_locked_descendants = 0

    def is_locked(self):
        return self.locked

    def _can_toggle_lock(self):
        """Returns wether or not this node can be locked or unlocked.

        A node can be locked or unlocked if all its descendants and 
        ancestors are not locked.

        Returns:
            True if it can be toggled, False if not.
        """
    
        if self.num_locked_descendants > 0:
            return False

        curr = self
        while curr.parent is not None:
            if curr.locked:
                return False
            curr = curr.parent

        return True

    def lock(self):
        """Locks this node if it can be locked.

        A node can be locked if all its descendants and ancestors are unlocked.
        If the node is already locked, it remains locked.

        Returns:
            True if it can be locked, False if not.
        """

        if not self._can_toggle_lock():
            return False

        if not self.locked:
            curr = self.parent
            while curr is not None:
                curr.num_locked_descendants += 1
                curr = curr.parent

        self.locked = True

        return True

    def unlock(self):
        """Unlocks this node if it can be unlocked.

        A node can be unlocked if all its descendants and ancestors are
        unlocked.
        If the node is already unlocked, it remains unlocked.

        Returns:
            True if it can be unlocked, False if not.
        """

        if not self._can_toggle_lock():
            return False

        if self.locked:
            curr = self.parent
            while curr is not None:
                curr.num_locked_descendants -= 1
                curr = curr.parent
        
        self.locked = False

        return False
