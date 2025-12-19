CREATE_PUR = """
    CREATE TABLE IF NOT EXISTS purs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pur TEXT NOT NULL, 
        buyed INTEGER DEFAULT 0
    ) 
"""
INSERT = "INSERT INTO purs (pur) VALUES (?)"

SELECT = 'SELECT id, pur, buyed FROM purs'

SELECT_PUR_BUY = 'SELECT id, pur, buyed FROM purs WHERE buyed = 1'

SELECT_PUR_NOT = 'SELECT id, pur, buyed FROM purs WHERE buyed = 0'

UPDATE_PUR = 'UPDATE purs SET pur = ? WHERE id = ?'

DELETE_PUR = "DELETE FROM purs WHERE id = ?"