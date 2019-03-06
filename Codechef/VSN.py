import java.util.*;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        double t= sc.nextInt();
        while(t-->0){
            double x1 = sc.nextInt();
            double y1 = sc.nextInt();
            double z1 = sc.nextInt();
            double a = sc.nextInt();
            double b = sc.nextInt();
            double c = sc.nextInt();
            double d = sc.nextInt();
            double e = sc.nextInt();
            double f = sc.nextInt();
            double x3 = sc.nextInt();
            double y3 = sc.nextInt();
            double z3 = sc.nextInt();
            double r = sc.nextInt();
            double P,Q,R,X,Y,Z,C,aa,bb,cc;
		P=a-x1; Q=b-y1; R=c-z1; 
		X = x1-x3; Y= y1-y3; Z = z1-z3;
		C = ((X*X)+(Y*Y)+(Z*Z));
		C -= (r*r);
		double n1,n2,n3;
		n1 = X*X - C; n2 = Y*Y - C; n3 = Z*Z - C;
		aa = d*d*n1;
		aa += e*e*n2;
		aa += f*f*n3;
		aa += ((2*X*Y*d*e)+(2*Y*Z*f*e)+(2*Z*X*d*f));
		bb = ((2*P*d*n1) +(2*Q*e*n2) +(2*R*f*n3));
		bb += 2*X*Y*(P*e + Q*d);
		bb += 2*Y*Z*(Q*f + R*e);
		bb += 2*X*Z*(P*f + R*d);
		cc = (P*P*n1) +(Q*Q*n2) +(R*R*n3);
		cc += 2*P*Q*X*Y;
		cc += 2*Y*Z*Q*R;
		cc += 2*Z*X*P*R;
	if(aa==0){
		double asd = -cc/bb;
		System.out.printf("%.10f%n",asd);
	}
	else {
		double di;
		di = bb*bb - 4*aa*cc;
		if(di>0){
			double ans = (-bb - Math.sqrt(di)) / (2*aa);
			if(ans>0){
				System.out.printf("%.10f%n",ans);
			}
			else{
				double yi = (-bb + Math.sqrt(di)) / (2*aa);
				System.out.printf("%.10f%n",yi);
			}	
				}
		if(di==0){
			double ans1 = -bb / (2*aa);
			System.out.printf("%.10f%n",ans1);
		}
	}
        }
    }
}
