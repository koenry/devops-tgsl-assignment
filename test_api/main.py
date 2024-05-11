import requests


class ServiceOrderClient:
    BASE_URL = "http://localhost:8000/serviceorders/"

    def __init__(self):
        self.session = requests.Session()

    def create_service_order(self, description, status):
        data = {"description": description, "status": status}

        response = self.session.post(self.BASE_URL, json=data)
        if response.status_code == 200:
            data = response.json()
            print(f'New order: {data["id"]} created')
            return data
        else:
            raise Exception(f'Error {response.status_code}')
        
    def get_created_order_status(self, new_order):
        url = f'{self.BASE_URL}{new_order}'
        response = requests.get(url)
        
        if response.status_code == 200:
            status = response.json()['status']
            print(status)
            return status
        else: 
            raise Exception(f'Error: {response.status_code}')

    def update_service_order(self, data):
        url = f'{self.BASE_URL}{new_order["id"]}'
        data['status'] = 'done'
        response = requests.patch(url, json=data)
        if response.status_code != 200:
            raise Exception(f'Error: {response.status_code}')

    def delete_service_order(self, data):
        url = f'{self.BASE_URL}{new_order["id"]}'
        response = requests.delete(url)
        if response.status_code != 204:
            raise Exception(f'Error: {response.status_code}')


if __name__ == "__main__":
    client = ServiceOrderClient()
    
    description = 'TGSL order'
    status = 'pending'
    
    new_order = client.create_service_order(description, status)
    status = client.get_created_order_status(new_order['id'])
    client.update_service_order(new_order)

    status = client.get_created_order_status(new_order['id'])
    print(status)
    client.delete_service_order(new_order)
    status = client.get_created_order_status(new_order['id'])
    print(status)
