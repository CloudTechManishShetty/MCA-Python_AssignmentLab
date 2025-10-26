# library/members.py

member_list = {}
member_id_counter = 1001

def register_member(name):
    global member_id_counter
    member_list[member_id_counter] = {"name": name, "status": "Active"}
    print("Member registered: ",name," with ID ",member_id_counter)
    member_id_counter += 1
    return member_id_counter - 1

def update_member_status(member_id, new_status):
    if member_id in member_list:
        member_list[member_id]['status'] = new_status
        print("Member ",member_id," status updated to ",new_status)
    else:
        print("Error: Member ID ",member_id," not found.")

def get_member_details(member_id):
    return member_list.get(member_id, "Member not found.")