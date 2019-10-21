

class Day(Base):
    __tablename__ = 'kalender'

    date = Column(String(8), primary_key=True)  """format: ddmmyyyy"""
    hari = Column(String(10), nullable=False)   """nama hari(ex: Senin)"""
    isHaribesar = Column(Boolean, nullable=False)   """apakah ada hari besar pada hari itu"""
    haribesar = Column(String(100))                 """deskripsi hari besar(jika ada)"""
    
    @property
    def serialize(self):
        return{
            'date': self.date,
            'hari': self.hari,
            'haribesar': self.haribesar,
            'isHaribesar': self.isHaribesar,
        }
    