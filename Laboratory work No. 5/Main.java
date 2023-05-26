package LW_8;
import java.sql.*;

class MysqlCon{
    public static void main(String args[]){
        try{
            Class.forName("com.mysql.jdbc.Driver");
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

            // Вызов функции
            CallableStatement stmt2 = con.prepareCall("{ ? = call count_lessons_by_teacher (?) }");
            stmt2.setInt(2, 2);
            stmt2.registerOutParameter(1, Types.INTEGER);
            stmt2.execute();
            int result = stmt2.getInt(1);
            System.out.println(result);
            stmt2.close();
            con.close();
        }
        catch(Exception e){ System.out.println(e);}
    }




}
