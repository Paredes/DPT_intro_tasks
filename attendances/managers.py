from base.managers import QuerySet


class AttendanceQuerySet(QuerySet):

    def search(self, query):
        """
        Search Attendance objects by name
        """
        if query:
            # TODO implement this method, since this is an example
            return self.filter(
                name__unaccent__icontains=query
            )
