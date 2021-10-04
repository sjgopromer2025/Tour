package tourDTO;
import tourVO.mapVO;

public class mapDTO extends CommonDTO
{
	private mapVO vo ;

	public void setVo(mapVO vo) {		this.vo = vo;	}
	
	public boolean load_map_element()
	{
		String x = "";
		String y = "";
		String place= "";
		try
		{

			String[] data_arr = this.vo.getData().split(",");
			String sql = "";
			sql += "select c_x, c_y, c_place from course ";
			sql += "where c_city = '"+ this.vo.getCity() +"' and ";
			String or_text = "";
			for (int i = 0; i < data_arr.length; i++) 
			{
				//��ǥ  x,y �� ��� ��
//				String[] coordinate = load_map(data_arr[i]);
//				if(i != data_arr.length-1) 
//				{
//					x += coordinate[0] + ",";
//					y += coordinate[1] + ",";
//				}else
//				{
//					x += coordinate[0] ;
//					y += coordinate[1] ;
//				}
				if(i < data_arr.length-1)
				{
					or_text += "c_place = '"+data_arr[i]+"' or ";
				}else
				{
					or_text += "c_place = '"+data_arr[i]+"' ";
				}
			}
			
			sql += "("+or_text+")";
			System.out.println(sql);
			this.OpenDB();
			this.RunQuery(sql);
			
			
			
			while(this.GetNextResult() == true)
			{
				x += this.GetValue("c_x") +",";
				y += this.GetValue("c_y") +",";
				place += this.GetValue("c_place")+",";
			}
			
			x = x.substring(0, x.length()-1);
			y = y.substring(0, y.length()-1);
			place = place.substring(0, place.length()-1);
			
			this.vo.setLat(x);
			this.vo.setLog(y);
			this.vo.setData(place);
			
			this.CloseQuery();
			this.CloseDB();
		}catch (Exception e) 
		{
			e.printStackTrace();
			return false;
		}
		
		return true;
	}
	
	
	public String[] load_map(String place)
	{
		String[] coordinate = new String[2];
		try
		{
			this.OpenDB();
			//select * from course where c_city='�ͻ�' and c_place like '%�̸�����%';
			//  c_x  c_y 
			String sql = "select c_x, c_y from course ";
			sql += "where c_city = '"+ this.vo.getCity() +"' and ";
			sql	+= "c_place= '"+place +"' ";
			
			this.RunQuery(sql);
			
			if(this.GetNextResult() == true)
			{
				coordinate[0] = this.GetValue("c_x");
				coordinate[1] = this.GetValue("c_y");
			}
			
			this.CloseQuery();
			this.CloseDB();
		}catch (Exception e) {
			e.printStackTrace();
			System.out.println("load_map����");
			return null;
		}
		
		
		return coordinate;
	}
	
	public static void main(String[] args)
	{
		
	}
}
