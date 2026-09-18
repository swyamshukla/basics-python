public class prac {
    public static void main(String[] args) {
        
        Employee empNew = new Manager(12, "swyam", 8480000, 'A', "first");

        empNew.getter();



    }
}
class Employee{
    int EmpID;
    String Name;
    int Salary;

    Employee(int EmpID, String Name, int Salary){
        this.EmpID=EmpID;
        this.Name=Name;
        this.Salary=Salary;
    }
    void setter(int EmpId,String Name, int Salary){
        this.EmpID=EmpID;
        this.Name=Name;
        this.Salary=Salary;
    }
    void getter(){
        System.out.println("Employee ID: "+EmpID);
        System.out.println("Employee Name: "+Name);
    }

}

class Manager extends Employee{
    char team;
    String cabin;
    Manager(int EmpID, String Name, int Salary,char team,String cabin){
        super(EmpID, Name, Salary);
        this.team=team;
        this.cabin=cabin;
    }
        void getter(){
            super.getter();
            System.out.println("Manager team :"+team);
            System.out.println("Manager cabin :"+cabin);

        }
}



