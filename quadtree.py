


class Rectangle:
    def __init__(self, x1, y1, x2, y2, center=None, node_id=None, parent_id=None, children_ids=None): # It contain these attributes: x1, y1, x2, y2, 
        """
        Initialize a rectangle with coordinates of bottom-left and top-right corners,
        and optionally include attributes for center point, node ID, parent node ID,
        and children node IDs.
        
        Parameters:
        - x1, y1: Coordinates of the bottom-left corner.
        - x2, y2: Coordinates of the top-right corner.
        - center: Tuple containing coordinates of the center point (optional).
        - node_id: ID of the current node (optional).
        - parent_id: ID of the parent node (optional).
        - children_ids: List of IDs of child nodes (optional).
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.center = center
        self.node_id = node_id
        self.parent_id = parent_id
        self.children_ids = children_ids

    def contains_point(self, x, y):
        """
        Check if a point (x, y) lies within the rectangle.
        
        Parameters:
        - x, y: Coordinates of the point.
        
        Returns:
        - True if the point lies within the rectangle, False otherwise.
        """
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2
