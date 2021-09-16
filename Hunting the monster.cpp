#include <iostream>
using namespace std;

class weap 
{
public :
	int pow = 0;
	int dur = 0;
};





int main() 
{
	int hp,n = 0;
	
	//입력받기
	
	cin >> hp;
	cin >> n;

	weap* weapon = new weap[n];

	for (int i = 0; i < n; i++)
	{
		cin >> weapon[i].pow >> weapon[i].dur;
	}

	//계산

	int sum = 0;
	int num = 0;
	
	while (sum <hp)
	{
		int max = 0;
		for (int i = 0; i < n; i++)
		{
			if (weapon[i].pow > weapon[max].pow)
				max = i;
		}

		if (weapon[max].pow * weapon[max].dur <= hp - sum)
		{
			num += weapon[max].dur;
			sum += weapon[max].pow * weapon[max].dur;
			weapon[max].pow = 0;
		}else
		{
			int j = 0;
			for(; sum < hp;j++ )
			{
				sum += weapon[max].pow;
			}
			num += j;
		}
	}

	cout << num;

}

