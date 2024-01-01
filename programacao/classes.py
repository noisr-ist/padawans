class IST:
  def __init__(self, nome: str, idade: int, ist: str) -> None:
    """Classe IST que representa uma pessoa do IST

    Args:
        nome (str): nome da pessoa
        idade (int): idade da pessoa
        ist (str): istID da pessoa
    """
    self._nome = nome
    self._idade = idade
    self._ist = ist
  
  #Getters & Setters
  def get_nome(self) -> str:
    """Getter do nome da pessoa

    Returns:
        str: nome da pessoa
    """
    return self._nome
  
  def get_idade(self) -> int:
    """Getter da idade da pessoa

    Returns:
        int: idade da pessoa
    """
    return self._idade

  def get_ist(self) -> str:
    """Getter do ist da pessoa

    Returns:
        str: istID da pessoa
    """
    return self._ist
  
  def set_nome(self, nome: str) -> None:
    """Setter do nome da pessoa

    Args:
        nome (str): novo nome da pessoa
    """
    self._nome = nome
  
  def set_idade(self, idade: int) -> None:
    """Setter da idade da pessoa

    Args:
        idade (int): nova idade da pessoa
    """
    self._idade = idade
  
  #Special Methods
  def __str__(self) -> str:
    """Método especial que retorna uma string com a informação da pessoa

    Returns:
        str: informação da pessoa
    """
    return f"Nome: {self._nome}\nIST: {self.ist}"
  
  def __repr__(self) -> str:
    """Método especial que retorna uma string com a informação da pessoa

    Returns:
        str: informação da pessoa
    """
    return f"Nome: {self._nome}\nIST: {self.ist}"
  
  def __eq__(self, other: object) -> bool:
    """Método especial que compara duas pessoas

    Args:
        other (object): pessoa a comparar 
        
    Returns:
        bool: True se forem iguais, False caso contrário
    """
    if not isinstance(other, IST):
      return False
    return self._nome == other._nome and self.ist == other.ist

class Professor(IST):
  def __init__(self, nome: str, idade: int, ist: str) -> None:
    """Classe Professor que representa um professor do IST

    Args:
        nome (str): nome do professor
        idade (int): idade do professor
        ist (str): istID do professor
    """
    super().__init__(nome, idade, ist)
    self._tutorandos = []
    
  #Getters & Setters
  def get_tutorandos(self) -> list:
    """Getter dos tutorandos do professor

    Returns:
        list: lista de tutorandos do professor
    """
    return self._tutorandos
  
  #Special Methods
  def __str__(self) -> str:
    """Método especial que retorna uma string com a informação do professor

    Returns:
        str: informação do professor
    """
    return f"Nome: {self._nome}\nTutorandos: {self._tutorandos}\nIST: {self.ist}"
  
  def __repr__(self) -> str:
    """Método especial que retorna uma string com a informação do professor

    Returns:
        str: informação do professor
    """
    return f"Nome: {self._nome}\nTutorandos: {self._tutorandos}\nIST: {self.ist}"


class Aluno(IST):
  def __init__(self, nome: str, idade: int, ist: str, curso: str, ano: int, tutor: Professor) -> None:
    """Classe Aluno que representa um aluno do IST

    Args:
        nome (str): nome do aluno
        idade (int): idade do aluno
        ist (str): istID do aluno
        curso (str): curso do aluno
        ano (int): ano do aluno
        tutor (Professor): tutor do aluno
    """
    super().__init__(nome, idade, ist)
    self._curso = curso
    self._ano = ano
    self._cadeiras = []
    self._tutor = ""
    tutor.add_tutorando(self)
  
  #Getters & Setters
  def get_curso(self) -> str:
    """Getter do curso do aluno

    Returns:
        str: curso do aluno
    """
    return self._curso
  
  def get_ano(self) -> int:
    """Getter do ano do aluno

    Returns:
        int: ano do aluno
    """
    return self._ano
  
  def get_cadeiras(self) -> list:
    """Getter das cadeiras do aluno

    Returns:
        list: lista de cadeiras do aluno
    """
    return self._cadeiras
  
  def set_curso(self, curso: str) -> None:
    """Setter do curso do aluno

    Args:
        curso (str): novo curso do aluno
    """
    self._curso = curso
  
  def set_ano(self, ano: int) -> None:
    """Setter do ano do aluno

    Args:
        ano (int): novo ano do aluno
    """
    self._ano = ano
    
  def set_tutor(self, tutor: Professor) -> None:
    """Setter do tutor do aluno

    Args:
        tutor (Professor): novo tutor do aluno
    """
    self._tutor = tutor
  
  #Special Methods
  def __str__(self) -> str:
    """Método especial que retorna uma string com a informação do aluno

    Returns:
        str: informação do aluno
    """
    return f"Nome: {self._nome}\nCurso: {self.curso}\nAno: {self.ano}\nIST: {self.ist}\nTutor: {self._tutor}"
  
  def __repr__(self) -> str:
    """Método especial que retorna uma string com a informação do aluno

    Returns:
        str: informação do aluno
    """
    return f"Nome: {self._nome}\nCurso: {self.curso}\nAno: {self.ano}\nIST: {self.ist}\nTutor: {self._tutor}"
  
  #Methods
  def add_cadeira(self, cadeira: str) -> None:
    """Método que adiciona uma cadeira ao aluno

    Args:
        cadeira (str): nome da cadeira
    """
    self.cadeiras.append(cadeira)
    

#Este método tem que ser definido fora da classe, porque a classe aluno ainda não estava definida quando a classe professor foi definida
def add_tutorando(self, aluno: Aluno) -> None:
  """Método que adiciona um tutorando ao professor

  Args:
      aluno (Aluno): aluno a adicionar
  """
  self.tutorandos.append(aluno)
  Aluno.set_tutor(self, self._nome)

def remove_tutorando(self, aluno: Aluno) -> None:
  """Método que remove um tutorando do professor

  Args:
      aluno (Aluno): aluno a remover
  """
  self.tutorandos.remove(aluno)
  Aluno.set_tutor(self, "")

Professor.add_tutorando = add_tutorando
Professor.remove_tutorando = remove_tutorando
