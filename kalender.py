

class Day(Base):
    __tablename__ = 'kalender'

    date = Column(String(8), primary_key=True)
    hari = Column(String(10), nullable=False)
    isHaribesar = Column(Boolean, nullable=False)
    haribesar = Column(String(100))
    
    @property
    def serialize(self):
        return{
            'date': self.date,
            'hari': self.hari,
            'haribesar': self.haribesar,
            'isHaribesar': self.isHaribesar,
        }
    