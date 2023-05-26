# Report | Отчет
1. Продемонстрировать выполнение запросов и хранимых процедур с помощью «таблично-запросного» API (любой, кроме PHP)
   + Выборка данных
   + Выполнение хранимой процедуры
   + Выполнение функции

-----
```Java
package LW_8;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

class MysqlCon{
    public static void main(String args[]){
        try{
//            Class.forName("com.mysql.jdbc.Driver");
            Connection con=DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/shedule","root","kamil");
                    Statement stmt=con.createStatement();
            ResultSet rs=stmt.executeQuery("select * from teachers");

            while (rs.next()) {
                int id = rs.getInt("ID");
                String name = rs.getString("Fullname");
                System.out.println(id + ": " + name);
            }
            rs.close();
            stmt.close();
            con.close();
        }catch(Exception e){ System.out.println(e);}
    }
}
```
Результат:
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/e4a52bba-31b5-44b3-8109-2c14937eef2e)
```Java
// Объект хранимой процедуры
CallableStatement callableStatement = con.prepareCall("{call get_disciplines_by_group(?)}");

// параметры для хранимой процедуры
callableStatement.setString(1, "Ежики");

// запуск хранимой процедуры
callableStatement.execute();

// получение результатов
ResultSet resultSet = callableStatement.getResultSet();
while (resultSet.next()) {
    String discipline = resultSet.getString("DisciplineName");
    System.out.println(discipline);
}
// закрыть объекты
resultSet.close();
callableStatement.close();
```
Результат
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/7ce98524-e458-4254-8b4e-2a68e3d8f2ad)

```Java
// Вызов функции
CallableStatement stmt = con.prepareCall("{ ? = call count_lessons_by_teacher (?) }");
stmt.setInt(2, 2);
stmt.registerOutParameter(1, Types.INTEGER);
stmt.execute();
int result = stmt.getInt(1);
System.out.println(result);
stmt.close();
```
Результат:
![image](https://github.com/Lszoa/Databases-and-information-systems/assets/115508876/ca7df607-e7b6-4fb8-9c2b-c200236dd5e6)
